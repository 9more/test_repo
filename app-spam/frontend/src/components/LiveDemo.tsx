import SpamForm from "./SpamForm";
import SentimentForm from "./SentimentForm";
import InsuranceForm from "./InsuranceForm";
import InsuranceRiskForm from "./InsuranceRiskForm";

type Props = {
    slug: string;
};

function LiveDemo({ slug }: Props) {

    switch (slug) {

        case "spam-email-detection":

            return <SpamForm />;

        case "sentiment-analysis":

            return <SentimentForm />;

        case "medical-insurance-charge-estimator":
            return <InsuranceForm />;

        case "insurance-risk-classifier":

             return <InsuranceRiskForm />;

        default:

            return (

                <div className="card">

                    <div className="card-body text-center">

                        <h4>
                            Live Demo Coming Soon
                        </h4>

                        <p className="mb-0 text-secondary">
                            This project is currently being
                            prepared for deployment.
                        </p>

                    </div>

                </div>

            );
    }
}

export default LiveDemo;